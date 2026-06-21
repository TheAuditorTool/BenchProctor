# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


async def BenchmarkTest21244(request: Request):
    path_value = request.path_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(path_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = path_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
