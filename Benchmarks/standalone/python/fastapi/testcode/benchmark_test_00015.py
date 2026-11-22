# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import urllib.parse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00015")
async def BenchmarkTest00015(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JSONResponse({'status': 'ok'})
    resp.headers['set-cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
