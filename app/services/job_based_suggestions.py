import json
import os
from google import genai
from google.genai.errors import APIError
from typing import Dict, Any, Optional
from dotenv import load_dotenv # Added import for python-dotenv

def ai_suggestions(input_data: Dict[str, Any], client: Optional[genai.Client] = None) -> Dict[str, Any]:
    """
    Performs unified ATS scoring, skill matching, and generates resume improvement 
    suggestions based on the provided resume data and job description, 
    returning the result as a structured JSON object.

    Args:
        input_data: A dictionary containing 'resume' (with 'extracted_data') 
                    and 'job_description' text.
        client: The initialized google.genai.Client object. If None, the function 
                will attempt to create a client using the GEMINI_API_KEY environment 
                variable as a fallback.

    Returns:
        A dictionary containing the ATS score, matched/missing skills, 
        and detailed suggestions, or an error dictionary.
    """
    
    # --- CRITICAL FALLBACK LOGIC ---
    if client is None:
        try:
            # Attempt to initialize client using environment variable
            load_dotenv() # Load .env file contents to make sure GEMINI_API_KEY is available
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                return {"error": "API Client not provided, and GEMINI_API_KEY environment variable is missing for fallback."}
            client = genai.Client(api_key=api_key)
        except Exception as e:
            return {"error": f"Failed to initialize Gemini client during fallback: {e}"}
    # --- END FALLBACK LOGIC ---

    try:
        # 1. Extract and Prepare Data
        resume_data = input_data.get("resume", {}).get("extracted_data", {})
        job_desc_text = input_data.get("job_description", "")
        
        # Check if essential data is missing
        if not resume_data or not job_desc_text:
            return {"error": "Missing 'resume' extracted data or 'job_description' text in input."}

        # Convert the structured resume data to a readable string for the model
        data_for_prompt = {
            "Skills": resume_data.get("skills", []),
            "Experience": [
                {k: v for k, v in exp.items() if k in ['company', 'title', 'details']}
                for exp in resume_data.get("experience", [])
            ],
            "Projects": [
                {k: v for k, v in proj.items() if k in ['project_name', 'details']}
                for proj in resume_data.get("projects", [])
            ]
        }
        resume_summary_str = json.dumps(data_for_prompt, indent=2)

    except (KeyError, AttributeError) as e:
        return {"error": f"Input data structure is incorrect: {e}"}

    # --- 2. Construct the Comprehensive Prompt ---
    prompt = f"""
    You are an expert Resume Analyst. Your task is to perform two actions based on the provided data:
    
    1.  **ATS Analysis & Scoring:** Analyze the RESUME DATA against the JOB DESCRIPTION.
        * Calculate an **ATS Score** (out of 100) based on keyword match, skill relevance, and experience alignment.
        * Identify all **Matched Skills** (skills present in both the resume and job description).
        * Identify all **Missing Skills** (critical skills from the job description not explicitly in the resume).
    
    2.  **Suggestion Generation:** Generate **detailed, actionable advice** for the user to improve their resume, focusing specifically on the Missing Skills.

    **RESUME DATA:**
    {resume_summary_str}

    **JOB DESCRIPTION (Target Role: Cybersecurity Analyst):**
    {job_desc_text}

    **REQUIRED OUTPUT FORMAT:**
    Your final response MUST be a single JSON object (DO NOT include any explanation or prose outside the JSON) that strictly adheres to the following structure:
    
    {{
        "ats_score": integer,
        "matched_skills": list of strings,
        "missing_skills": list of strings,
        "suggestions": {{
            "score_analysis": string,
            "strengths_to_highlight": string,
            "missing_skills_advice": string,
            "general_improvements": string
        }}
    }}
    
    Ensure the advice is professional, encouraging, and highly specific to the content provided, guiding the user on rephrasing their existing experience to align better with the security role.
    """
    
    # --- 3. Call the Gemini API with JSON Output Constraint ---
    try:
        # The 'client' is now guaranteed to be initialized here (either passed or created).
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        
        # The response text will be a JSON string, which we parse into a dict
        return json.loads(response.text)
        
    except APIError as e:
        return {"error": f"Gemini API Error: {e}"}
    except json.JSONDecodeError as e:
        # Includes raw response for easier debugging if model output is malformed
        return {"error": f"Failed to decode JSON response from AI: {e}", "raw_response": response.text}
    except Exception as e:
        return {"error": f"An unexpected error occurred during API call: {e}"}
