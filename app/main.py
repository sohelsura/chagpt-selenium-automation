import time

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db
from .chatgpt_automation import ChatGPTAutomation
from config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
chatgpt = ChatGPTAutomation(settings.CHROME_PATH, settings.CHROME_DRIVER_PATH)

@app.get("/prompts/", response_model=list[schemas.Prompt])
def read_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prompts = crud.get_prompts(db, skip=skip, limit=limit)
    return prompts

@app.post("/process_prompts/")
def process_prompts(prompt: schemas.PromptCreate, db: Session = Depends(get_db)):
    
    try:
        prompt = crud.create_prompt(db=db, prompt=prompt)
        chatgpt.send_prompt_to_chatgpt(prompt.prompt)
        last_conversation = chatgpt.return_last_response()
        crud.update_prompt(db, prompt.id, last_conversation)
        return {"message": last_conversation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))