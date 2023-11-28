from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from database import SessionLocal

from models import Author, Book, News
from schema import AuthorCreate, BookCreate, NewsCreate

app = FastAPI()

books = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Авторы
@app.post("/authors/")
async def create_author(author: AuthorCreate):
    db = SessionLocal()
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return {"author": new_author}


@app.get("/authors/")
async def get_authors():
    db = SessionLocal()
    authors = db.query(Author).all()
    return {"authors": authors}

#Книги
@app.post("/books/")
async def create_book(book: BookCreate):
    db = SessionLocal()
    new_book = Book(title=book.title, author_id=book.author_id, genre=book.genre, img=book.img)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"book": new_book}


@app.get("/books/")
async def get_books():
    db = SessionLocal()
    books = db.query(Book).all()
    return {"books": books}

#Новости
@app.post("/news/")
async def create_news(news: NewsCreate):
    db = SessionLocal()
    new_news = News(title=news.title, content=news.content)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return {"news": new_news}

@app.get("/news/")
async def get_news():
    db = SessionLocal()
    news = db.query(News).all()
    return {"news": news}
