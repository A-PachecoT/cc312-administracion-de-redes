from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class User(BaseModel):
    user: str

@app.post("/count")
async def count_user(user_data: User):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                'http://api2:5001/register', 
                json={'user': user_data.user}
            )
            return response.json()
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Error al comunicarse con API 2")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000) 