# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import requests


async def BenchmarkTest63875(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return {"updated": True}
