# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast


async def BenchmarkTest72253(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
