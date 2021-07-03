from pydantic import BaseModel


class Domain(BaseModel):
    name: str
    total_pages: int = 0
    document_count: int = 0
    classified: bool = False
