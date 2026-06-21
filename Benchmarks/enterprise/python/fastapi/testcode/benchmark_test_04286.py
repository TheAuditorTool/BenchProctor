# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import ast


async def BenchmarkTest04286(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
