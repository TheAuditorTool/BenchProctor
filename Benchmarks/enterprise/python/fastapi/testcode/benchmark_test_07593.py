# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import defusedxml.ElementTree


async def BenchmarkTest07593(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
