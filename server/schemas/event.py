from pydantic import BaseModel

class EventRequest(BaseModel):
    id: int
    name: str
    completed: bool

class EventResponse(BaseModel):
    id: int
    name: str
    completed: bool

    class Config:
        orm_mode = True
            