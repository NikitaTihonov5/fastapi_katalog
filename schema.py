from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str
    author_id: int
    genre: str
    img: str

class NewsCreate(BaseModel):
    title: str
    content: str