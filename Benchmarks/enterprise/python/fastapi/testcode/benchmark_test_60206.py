# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import defusedxml.ElementTree


async def BenchmarkTest60206(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
