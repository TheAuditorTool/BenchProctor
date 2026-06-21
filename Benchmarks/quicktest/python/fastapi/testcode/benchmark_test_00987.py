# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest00987(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
