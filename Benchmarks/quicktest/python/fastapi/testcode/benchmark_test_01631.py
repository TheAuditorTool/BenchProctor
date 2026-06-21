# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest01631(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
