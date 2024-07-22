from sqlalchemy.orm import Session

from . import models, schemas

def get_prompts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prompt).offset(skip).limit(limit).all()

def create_prompt(db: Session, prompt: schemas.PromptCreate):
    db_prompt = models.Prompt(prompt=prompt.prompt)
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

def get_unprocessed_prompts(db: Session):
    return db.query(models.Prompt).filter(models.Prompt.processed == False).all()

def update_prompt(db: Session, prompt_id: int, response: str| None):
    db_prompt = db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()
    if db_prompt:
        db_prompt.response = response
        db_prompt.processed = True
        db.commit()
        db.refresh(db_prompt)
    return db_prompt