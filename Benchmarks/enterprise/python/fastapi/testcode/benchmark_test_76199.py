# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import ast


async def BenchmarkTest76199(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    processed = str(data).replace("<script", "")
    return HTMLResponse('<img src="' + str(processed) + '">')
