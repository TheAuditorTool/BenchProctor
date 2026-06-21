# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest08890(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
