# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from http.cookies import SimpleCookie
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00268")
async def BenchmarkTest00268(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    cookie = SimpleCookie()
    cookie['session'] = str(data)
    cookie['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    resp = JSONResponse({'status': 'ok'})
    resp.headers.append('set-cookie', cookie['session'].OutputString())
    return resp
