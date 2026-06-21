# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest64225(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
