# main.py

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

from backup import main as backup_main

app = FastAPI()


class BackupRequest(BaseModel):
    username: str


def run_backup(username: str):
    backup_main(username)


@app.post("/backup")
async def backup(request: BackupRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_backup, request.username)
    return {"message": "Backup request has been accepted. Changed."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)