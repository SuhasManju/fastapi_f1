from fastapi import FastAPI

app=FastAPI(debug=False)

@app.get("/")
def main_call():
    return {"message":"main app"}
