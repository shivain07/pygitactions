import os

def send_mail(workflow_name,repo_name,email,username):
    print(f"Workflow name {workflow_name} repo name {repo_name}")
    print(f"DEMO MAIL SENT to {username} via {email}")

send_mail(os.getenv("WORKFLOW_NAME"),os.getenv("REPO_NAME"),os.getenv("EMAIL"),os.getenv("USERNAME"))