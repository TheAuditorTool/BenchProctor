# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
import ast


async def BenchmarkTest58995(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
