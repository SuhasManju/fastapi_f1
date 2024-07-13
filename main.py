from fastapi import FastAPI,APIRouter
from dashboard.dashboard import dashbboard

app=FastAPI(debug=True)
app_router=APIRouter()

app_router.include_router(dashbboard)

app.include_router(app_router)
