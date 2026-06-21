# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02791(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
