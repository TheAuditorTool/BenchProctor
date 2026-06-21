# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


async def BenchmarkTest65649(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = header_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
