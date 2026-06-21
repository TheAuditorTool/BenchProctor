# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast


async def BenchmarkTest39446(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
