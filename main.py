from fastapi import FastAPI
from app.authors.router import router as router_authors
from app.categories.router import router as router_categories
from app.posts.router import router as router_posts
from app.database import engine, Base

app = FastAPI()

app.include_router(router_authors)
app.include_router(router_categories)
app.include_router(router_posts)


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
