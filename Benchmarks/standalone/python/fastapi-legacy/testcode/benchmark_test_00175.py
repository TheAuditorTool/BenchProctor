# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap3
import os
from app_runtime import db
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00175")
async def BenchmarkTest00175(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(data) + ')', attributes=['cn'])
    return {"updated": True}
