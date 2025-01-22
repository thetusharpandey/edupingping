from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        return FileResponse("index.html")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/sex", response_class=HTMLResponse)
async def read_sex():
    try:
        return FileResponse("revenue.html")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/hashgen.html", response_class=HTMLResponse)
async def read_hashgen():
    try:
        return FileResponse("hashgen.html")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/pets.gif")
async def read_pets():
    try:
        return FileResponse("pets.gif", media_type="image/gif")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/babay.gif")
async def read_babay():
    try:
        return FileResponse("babay.gif", media_type="image/gif")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/easyConcept.gif")
async def read_easy_concept():
    try:
        return FileResponse("easyConcept.gif", media_type="image/gif")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/moneySave.gif")
async def read_money_save():
    try:
        return FileResponse("moneySave.gif", media_type="image/gif")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/sadly4041.html", response_class=HTMLResponse)
async def read_sadly4041():
    try:
        return FileResponse("sadly4041.html")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")   

# Default handler for unmatched paths
@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("sadly404.html", media_type="text/html")

import nest_asyncio
import uvicorn

if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app, host="localhost", port=8069)
