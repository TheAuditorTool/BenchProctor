# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


async def BenchmarkTest62829(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = raw_body
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
