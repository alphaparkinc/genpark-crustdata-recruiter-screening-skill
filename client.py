class CrustdataRecruiterClient:
    def screen_candidate(self, resume_text: str, job_requirements: list[str]) -> dict:
        match_count = sum(1 for req in job_requirements if req.lower() in resume_text.lower())
        ratio = match_count / max(1, len(job_requirements))
        verdict = "STRONGLY MATCH" if ratio >= 0.8 else "CONSIDER" if ratio >= 0.5 else "REJECT"
        return {"match_score": round(ratio * 100, 1), "fit_verdict": verdict}