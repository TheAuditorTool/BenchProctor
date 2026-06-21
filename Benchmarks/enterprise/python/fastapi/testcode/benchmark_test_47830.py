# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import ast


async def BenchmarkTest47830(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
