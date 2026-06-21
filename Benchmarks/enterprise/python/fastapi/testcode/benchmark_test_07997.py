# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest07997(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
