# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest77439(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    result = 100 / int(str(data))
    return {"updated": True}
