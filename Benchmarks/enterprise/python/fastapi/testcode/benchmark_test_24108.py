# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import ast
from app_runtime import auth_check


async def BenchmarkTest24108(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
