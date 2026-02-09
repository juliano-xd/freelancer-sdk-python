from typing import Any


class Job:
    def __init__(
        self,
        id: int = 0,
        name: str = "",
        category: dict[int, str] = {},
        seo_url: str = "",
        local: bool = False,
    ):
        self.id: int = id
        self.name: str = name
        self.category: dict[int, str] = category
        self.seo_url: str = seo_url
        self.local: bool = local
        self.info: dict[str, Any]
