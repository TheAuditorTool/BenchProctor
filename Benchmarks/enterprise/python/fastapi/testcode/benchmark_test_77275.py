# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest77275(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
