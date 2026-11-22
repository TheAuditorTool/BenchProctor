# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap3
import re
from starlette.responses import JSONResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00028")
async def BenchmarkTest00028(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return {"updated": True}
