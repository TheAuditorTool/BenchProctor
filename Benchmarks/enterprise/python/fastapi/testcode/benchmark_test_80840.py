# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest80840(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    if not re.fullmatch('^[\\w\\s.*]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
