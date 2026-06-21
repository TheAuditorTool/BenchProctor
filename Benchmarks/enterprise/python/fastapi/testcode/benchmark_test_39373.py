# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import ast
from app_runtime import auth_check


async def BenchmarkTest39373(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    auth_check('user', data)
    return {"updated": True}
