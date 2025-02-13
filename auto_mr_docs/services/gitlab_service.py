from typing import Optional
import gitlab

class GitlabService:
    
    def __init__(self, private_token: Optional[str], project_id: int, base_url: str = "https://gitlab.com"):
        self.private_token = private_token
        self.project_id = project_id
        self.base_url = base_url

    def _get_project(self):
        try:
            gl = gitlab.Gitlab(self.base_url, private_token=self.private_token)
            return gl.projects.get(self.project_id)
        except gitlab.exceptions.GitlabGetError as e:
            raise ValueError(f"Failed to fetch project {self.project_id}: {e}")

    def get_merge_request_commits(self, mr_id: int) -> list[str]:
        try:
            project = self._get_project()
            mr = project.mergerequests.get(mr_id)
            return [commit.attributes["message"] for commit in mr.commits()]
        except gitlab.exceptions.GitlabGetError as e:
            raise ValueError(f"Failed to fetch commits for MR {mr_id}: {e}")

    def update_merge_request_description(self, mr_id: int, new_description: str) -> None:
        try:
            project = self._get_project()
            mr = project.mergerequests.get(mr_id)
            mr.description = new_description
            mr.save()
        except gitlab.exceptions.GitlabUpdateError as e:
            raise ValueError(f"Failed to update MR {mr_id} description: {e}")
