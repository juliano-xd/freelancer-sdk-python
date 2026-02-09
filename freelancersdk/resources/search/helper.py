from typing import Any

from freelancersdk.resources.search.exceptions import (
    JobsNotFoundException,
    UsersNotFoundException,
)
from freelancersdk.session import Session


def users_get_request(
    session: Session, endpoint: str, params_data: dict[str, Any] = {}
):
    user_url = f"{session.url}users/0.1/{endpoint}"
    response = session.session.get(user_url, params=params_data, verify=True)
    if response.status_code != 200:
        error = response.json()
        raise UsersNotFoundException(
            message=error.get("message", "Unknown error"),
            error_code=error.get("error_code", 0),
            request_id=error.get("request_id", "N/A"),
        )
    return response


def projects_get_request(
    session: Session, endpoint: str, params_data: dict[str, Any] = {}
):
    project_url = f"{session.url}projects/0.1/{endpoint}"
    response = session.session.get(project_url, params=params_data, verify=True)
    if response.status_code != 200:
        error = response.json()
        if endpoint.__contains__("jobs"):
            raise JobsNotFoundException(
                message=error.get("message", "Unknown error"),
                error_code=error.get("error_code", 0),
                request_id=error.get("request_id", "N/A"),
            )
    return response
