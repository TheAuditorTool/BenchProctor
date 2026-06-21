# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest29557(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
