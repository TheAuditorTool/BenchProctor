# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import ast


async def BenchmarkTest78240(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    def _primary():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
