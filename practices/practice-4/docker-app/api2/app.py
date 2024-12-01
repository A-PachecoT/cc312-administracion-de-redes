from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
from typing import Dict

app = FastAPI()

class User(BaseModel):
    user: str

async def get_db_pool():
    return await asyncpg.create_pool(
        host="db",
        database="userdb",
        user="postgres",
        password="postgres"
    )

@app.on_event("startup")
async def startup():
    app.state.pool = await get_db_pool()

@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()

@app.post("/register")
async def register_user(user_data: User) -> Dict[str, int]:
    async with app.state.pool.acquire() as conn:
        # Inserto el usuario
        await conn.execute(
            "INSERT INTO users (username) VALUES ($1)", 
            user_data.user
        )
        # Cuento ocurrencias
        count = await conn.fetchval(
            "SELECT COUNT(*) FROM users WHERE username = $1", 
            user_data.user
        )
        return {"count": count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001) 