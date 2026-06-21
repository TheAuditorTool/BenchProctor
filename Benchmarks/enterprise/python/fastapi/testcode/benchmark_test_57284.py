# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest57284(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
