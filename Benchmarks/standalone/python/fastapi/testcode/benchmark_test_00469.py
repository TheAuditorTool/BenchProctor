# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
from starlette.responses import JSONResponse
import re
from app_runtime import db


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00469")
async def BenchmarkTest00469(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return {"updated": True}
