# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


async def BenchmarkTest59171(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    globals()['counter'] = int(data)
    return {"updated": True}
