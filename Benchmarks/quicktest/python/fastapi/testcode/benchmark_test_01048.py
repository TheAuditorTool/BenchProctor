# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import ast


async def BenchmarkTest01048(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
