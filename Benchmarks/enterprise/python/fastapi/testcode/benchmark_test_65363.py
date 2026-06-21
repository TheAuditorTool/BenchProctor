# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import re
from dataclasses import dataclass
import os
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65363(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
