# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
import os
from starlette.responses import JSONResponse


async def BenchmarkTest05656(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = env_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
