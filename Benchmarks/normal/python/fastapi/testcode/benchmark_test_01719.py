# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest01719(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
