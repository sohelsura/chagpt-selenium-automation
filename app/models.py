from sqlalchemy import Column, Integer, String, Text, Boolean

from .database import Base

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String(500), nullable=False)
    response = Column(Text)
    processed = Column(Boolean, default=False)