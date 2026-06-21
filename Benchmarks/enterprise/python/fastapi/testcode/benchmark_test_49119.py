# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import ast


async def BenchmarkTest49119(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    json.loads(data)
    return {"updated": True}
