# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest75676(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    request.session['data'] = str(data)
    return {"updated": True}
