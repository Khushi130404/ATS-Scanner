import math

def calculate_score(matched_count: int, total_jd_skills: int) -> int:
    """
    Calculate score with an increasing pattern.
    Gives a boost when key skills are matched.
    """
    if total_jd_skills == 0:
        return 0
    
    ratio = matched_count / total_jd_skills

    score = 100 * (ratio ** 0.4)  

    return min(100, int(score))
