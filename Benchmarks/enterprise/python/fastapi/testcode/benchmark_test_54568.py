# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import ast


async def BenchmarkTest54568(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
