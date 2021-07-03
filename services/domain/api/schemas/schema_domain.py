from pydantic import BaseModel


class Domain(BaseModel):
    name: str
    total_pages: int = 0
    document_count: int = 0
    classified: bool = False


class DomainUpdate(BaseModel):
    domain_id: str
    name: str
    total_pages: int = 0
    document_count: int = 0
    classified: bool = False
