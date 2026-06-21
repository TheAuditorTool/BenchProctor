# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest65877(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = str(ast.literal_eval(config_value))
    except (ValueError, SyntaxError):
        data = config_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
