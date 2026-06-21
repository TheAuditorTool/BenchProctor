# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
import ast
from app_runtime import auth_check


async def BenchmarkTest09949(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
