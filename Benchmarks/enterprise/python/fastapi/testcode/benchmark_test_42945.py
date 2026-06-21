# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from app_runtime import auth_check


async def BenchmarkTest42945(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
