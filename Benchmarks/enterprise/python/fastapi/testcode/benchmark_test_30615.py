# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest30615(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    int(str(data))
    return {"updated": True}
