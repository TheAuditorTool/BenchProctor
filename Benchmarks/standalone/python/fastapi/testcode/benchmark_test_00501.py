# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap
import re
from starlette.responses import JSONResponse
import json
import os


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00501")
async def BenchmarkTest00501(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return {"updated": True}
