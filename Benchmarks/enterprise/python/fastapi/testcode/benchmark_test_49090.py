# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import defusedxml.ElementTree


async def BenchmarkTest49090(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
