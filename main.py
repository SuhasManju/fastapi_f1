from fastapi import FastAPI,APIRouter,Request
from dashboard.dashboard import dashbboard
from detailed_reports.detailed_reports import detailed_api
from quali_reports.quali_reports import quali_reports
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import logging
import time
from dotenv import load_dotenv
import os

load_dotenv()

debug=bool(os.getenv("debug"))

app=FastAPI(debug=debug)
app_router=APIRouter()

app_router.include_router(dashbboard)
app_router.include_router(detailed_api)
app_router.include_router(quali_reports)

app.include_router(app_router)

@app.get('/')
def redirect_to_docs():
    return RedirectResponse("http://127.0.0.1:8000/docs")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named app.log
    ]
)
logger=logging.getLogger(__name__)

@app.middleware("http")
async def add_process_time(request:Request,call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.2f}s")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
