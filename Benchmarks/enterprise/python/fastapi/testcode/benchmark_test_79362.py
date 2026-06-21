# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest79362(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    int(str(data))
    return {"updated": True}
