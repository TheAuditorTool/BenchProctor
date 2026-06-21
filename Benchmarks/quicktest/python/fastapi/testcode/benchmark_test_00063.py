# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import ast


async def BenchmarkTest00063(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    json.loads(data)
    return {"updated": True}
