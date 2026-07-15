from client import CrustdataRecruiterClient
client = CrustdataRecruiterClient()
print(client.screen_candidate("Experience in Python, SQL and RAG.", ["Python", "SQL", "Rust"]))