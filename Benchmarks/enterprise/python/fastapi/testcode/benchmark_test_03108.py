# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest03108(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
