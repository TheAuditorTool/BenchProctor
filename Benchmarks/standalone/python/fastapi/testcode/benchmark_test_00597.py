# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap
import re
from starlette.responses import JSONResponse
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


@app.post("/BenchmarkTest00597")
async def BenchmarkTest00597(request: Request):
    user_id = request.query_params.get('id', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", user_id):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = user_id
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, '(uid=' + str(processed) + ')')
    return {"updated": True}
