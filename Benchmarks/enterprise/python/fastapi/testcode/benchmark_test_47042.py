# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest47042(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
