# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest43001(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
