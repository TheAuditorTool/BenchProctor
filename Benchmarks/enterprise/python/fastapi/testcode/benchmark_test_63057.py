# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import auth_check


async def BenchmarkTest63057(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = str(ast.literal_eval(file_value))
    except (ValueError, SyntaxError):
        data = file_value
    auth_check('user', data)
    return {"updated": True}
