from local_model import LocalModel
from open_ai_api import OpenAIAPI

def main() -> None:
    commits = [
        "Add support for two-factor authentication (2FA) in login",
        "Fix issue where users could not reset their passwords",
        "Refactor user session management for better scalability",
        "Optimize database queries for fetching user profiles",
        "Fix incorrect validation on email field during signup",
        "Improve error messages in API responses",
        "Fix UI bug in the dashboard layout on mobile devices",
        "Add logs for tracking failed login attempts",
        "Enhance security by enforcing stronger password policies",
        "Refactor payment gateway integration for better maintainability"
    ]
    
    local_model = LocalModel()    
    print(local_model.generate_description_by_commits(commits))
    
    # open_ai = OpenAIAPI()
    # print(open_ai.generate_description_by_commits(commits))

if __name__ == '__main__':
    main()
