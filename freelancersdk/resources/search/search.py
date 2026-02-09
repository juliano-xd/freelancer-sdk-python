from typing import Any

from freelancersdk.resources.projects.jobs import Job
from freelancersdk.resources.search.helper import (
    projects_get_request,
    users_get_request,
)
from freelancersdk.resources.users.user import User
from freelancersdk.session import Session


class Search:
    def __init__(self, session: Session):
        self.session = session

    def get_self_user(self, user_details: dict[str, Any] = {}) -> User:
        """Get details about the currently authenticated user"""
        response = users_get_request(self.session, "self", user_details)
        return User(self.session, response.json().get("result", {}))

    def get_user_by_id(self, user_id: int, user_details: dict[str, Any] = {}) -> User:
        """Get details about specific user"""
        response = users_get_request(self.session, f"users/{user_id}", user_details)
        return User(self.session, response.json().get("result", {}))

    def get_users_by_ids(self, ids: set[int]) -> set[User]:
        """Get one or more users"""
        if not ids:
            return set()
        response = users_get_request(
            self.session, "users", params_data={"users[]": list(ids)}
        )
        result = response.json().get("result", {})
        users_data: dict[str, dict] = result.get("users", {})
        return {User(self.session, u) for u in users_data.values()}

    def get_users_by_usernames(
        self, usernames: set[str], params: dict = {}
    ) -> set[User]:
        if not usernames:
            return set()

        params["usernames[]"] = list(usernames)
        response = users_get_request(self.session, "users", params_data=params)
        result = response.json().get("result", {})
        users_data: dict[str, dict] = result.get("users", {})
        return {User(self.session, u) for u in users_data.values()}

    def get_jobs_by_ids(self, ids: set[int]) -> set[Job]:
        """Returns jobs with the specified job IDs."""
        if not ids:
            return set()
        response = projects_get_request(self.session, "jobs", {"jobs[]": list(ids)})
        json_data = response.json()
        return {
            Job(j["id"], j["name"], j["category"], j["seo_url"], j["local"])
            for j in json_data["result"]
        }

    def get_jobs_by_names(self, names: set[str]) -> set[Job]:
        """Returns jobs with the specified name."""
        if not names:
            return set()
        response = projects_get_request(
            self.session, "jobs", {"job_names[]": list(names)}
        )
        json_data = response.json()
        return {
            Job(j["id"], j["name"], j["category"], j["seo_url"], j["local"])
            for j in json_data["result"]
        }

    def get_jobs_by_seo(self, seo: set[str]) -> set[Job]:
        """Returns jobs with the specified SEO URLs."""
        if not seo:
            return set()
        response = projects_get_request(self.session, "jobs", {"seo_urls[]": list(seo)})
        json_data = response.json()
        return {
            Job(j["id"], j["name"], j["category"], j["seo_url"], j["local"])
            for j in json_data["result"]
        }

    def get_jobs_by_categories(self, ids: set[int]) -> set[Job]:
        """Returns jobs within a specific category."""
        if not ids:
            return set()
        response = projects_get_request(
            self.session, "jobs", {"categories[]": list(ids)}
        )
        json_data = response.json()
        return {
            Job(j["id"], j["name"], j["category"], j["seo_url"], j["local"])
            for j in json_data["result"]
        }

    def get_only_local_jobs(self, params: dict[str, Any] = {}) -> set[Job]:
        """Returns only local jobs"""
        params["only_local"] = True
        response = projects_get_request(self.session, "jobs", params)
        json_data = response.json()
        return {
            Job(j["id"], j["name"], j["category"], j["seo_url"], j["local"])
            for j in json_data["result"]
        }
