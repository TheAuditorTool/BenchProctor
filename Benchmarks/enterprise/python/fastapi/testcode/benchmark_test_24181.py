# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


async def BenchmarkTest24181(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = xml_value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
