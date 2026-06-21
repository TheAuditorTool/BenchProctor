# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


request_state: dict[str, str] = {}

async def BenchmarkTest51841(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
