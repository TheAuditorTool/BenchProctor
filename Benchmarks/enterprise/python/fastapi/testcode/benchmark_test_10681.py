# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import json


request_state: dict[str, str] = {}

async def BenchmarkTest10681(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
