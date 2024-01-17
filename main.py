import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models import board_model
from db.connection import engine
from routers import board_routers as b_router
from routers import user_routers as u_router


board_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-process-Time"] = str(process_time)
    return response


app.include_router(b_router.app, tags=["board"])
app.include_router(u_router.app, tags=["user"])


@app.get("/")
def root():
    return {"Welcome to my first FastAPI CRUD Board"}
