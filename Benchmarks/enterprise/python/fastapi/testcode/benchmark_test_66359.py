# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


async def BenchmarkTest66359(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    globals()['counter'] = int(data)
    return {"updated": True}
