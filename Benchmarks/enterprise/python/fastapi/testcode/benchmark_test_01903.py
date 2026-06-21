# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast


async def BenchmarkTest01903(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
