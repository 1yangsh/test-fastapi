from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "안녕"}


@app.get("/home")
async def main():
    return {"message": "This is a homepage"}


@app.get("/user/{user_id}")
async def main(user_id):
    return {"message": f"user {user_id} 입니다.",
            "video": "https://www.s3.com"}