# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from starlette.responses import JSONResponse


async def BenchmarkTest07890(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
