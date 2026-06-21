# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest49353(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
