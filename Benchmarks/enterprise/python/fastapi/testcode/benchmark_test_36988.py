# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import json
import os


request_state: dict[str, str] = {}

async def BenchmarkTest36988(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
