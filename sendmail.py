import os

def send_mail(workflow_name,repo_name):
    print(f"Workflow name {workflow_name} repo name {repo_name}")
    print(f"DEMO MAIL SENT")

send_mail(os.getenv("WORKFLOW_NAME"),os.getenv("REPO_NAME"))