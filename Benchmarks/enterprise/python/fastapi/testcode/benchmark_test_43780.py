# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import json


async def BenchmarkTest43780(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    digest = hashlib.sha1(str(graphql_var).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
