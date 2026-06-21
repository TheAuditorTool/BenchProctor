# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest67807(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
