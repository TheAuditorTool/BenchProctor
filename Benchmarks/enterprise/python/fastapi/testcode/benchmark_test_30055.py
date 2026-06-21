# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest30055(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
