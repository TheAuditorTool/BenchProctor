# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest71534(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
