# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import defusedxml.ElementTree


async def BenchmarkTest53724(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
