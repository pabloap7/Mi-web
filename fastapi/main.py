from typing import Union

from fastapi import FastAPI, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/fincher", response_class=HTMLResponse)
async def fincher(request: Request):
     return templates.TemplateResponse(
         request=request, name="fincher.html"                                                    
     )

@app.get("/scorsese", response_class=HTMLResponse)
async def scorsese(request: Request):
     return templates.TemplateResponse(
         request=request, name="scorsese.html"                                                    
     )

@app.get("/tarantino", response_class=HTMLResponse)
async def tarantino(request: Request):
     return templates.TemplateResponse(
         request=request, name="tarantino.html"                                                    
     )

@app.get("/villeneuve", response_class=HTMLResponse)
async def villenueve(request: Request):
     return templates.TemplateResponse(
         request=request, name="villeneuve.html"                                                    
     )

@app.get("/spielberg", response_class=HTMLResponse)
async def spielberg(request: Request):
     return templates.TemplateResponse(
         request=request, name="spielberg.html"                                                    
     )

@app.get("/coppola", response_class=HTMLResponse)
async def coppola(request: Request):
     return templates.TemplateResponse(
         request=request, name="coppola.html"                                                    
     )