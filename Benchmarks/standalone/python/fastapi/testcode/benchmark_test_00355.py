# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap3
from starlette.responses import JSONResponse
import os
import re


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00355/{id}")
async def BenchmarkTest00355(request: Request, id: str):
    path_value = id
    if not re.fullmatch("^(asc|desc|name|created)$", str(path_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return {"updated": True}
