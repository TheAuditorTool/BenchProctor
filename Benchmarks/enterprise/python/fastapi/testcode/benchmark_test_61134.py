# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from app_runtime import auth_check


async def BenchmarkTest61134(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if not auth_check(request.session.get('user', ''), str(graphql_var)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
