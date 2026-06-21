# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import ast
from app_runtime import auth_check


async def BenchmarkTest76066(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
