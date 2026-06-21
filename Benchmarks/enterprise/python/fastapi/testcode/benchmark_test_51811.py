# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import ast


async def BenchmarkTest51811(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
