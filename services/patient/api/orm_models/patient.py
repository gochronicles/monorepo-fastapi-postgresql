from sqlalchemy import Column, String, DateTime, Integer, Boolean
from api import Base


class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    total_pages = Column(Integer)
    document_count = Column(Integer)
    classified = Column(Boolean)
    created_timestamp = Column(DateTime)
    updated_timestamp = Column(DateTime)
