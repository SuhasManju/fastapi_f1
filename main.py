from fastapi import FastAPI,APIRouter
from dashboard.dashboard import dashbboard
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(debug=True)
app_router=APIRouter()

app_router.include_router(dashbboard)

app.include_router(app_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
