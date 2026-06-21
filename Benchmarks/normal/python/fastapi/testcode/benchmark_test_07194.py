# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest07194(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
