from pydantic import BaseModel


class Domain(BaseModel):
    # domain_id: str
    name: str
    total_pages: int = 0
    document_count: int = 0
    classified: bool = False
