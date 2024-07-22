from pydantic import BaseModel

class PromptBase(BaseModel):
    prompt: str

class PromptCreate(PromptBase):
    pass

class Prompt(PromptBase):
    id: int
    response: str | None = None
    processed: bool

    class Config:
        orm_mode = True