# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap
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


@app.post("/BenchmarkTest00168")
async def BenchmarkTest00168(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % str(xml_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return {"updated": True}
