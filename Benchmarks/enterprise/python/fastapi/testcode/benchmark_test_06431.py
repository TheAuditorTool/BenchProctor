# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import time
import ast


async def BenchmarkTest06431(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
