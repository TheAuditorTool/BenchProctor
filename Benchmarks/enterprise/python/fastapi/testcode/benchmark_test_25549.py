# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import os
import ast


async def BenchmarkTest25549(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return {"updated": True}
