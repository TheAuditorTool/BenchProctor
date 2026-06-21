# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import ast


async def BenchmarkTest03159(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
