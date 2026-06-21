# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from starlette.responses import JSONResponse


async def BenchmarkTest57417(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
