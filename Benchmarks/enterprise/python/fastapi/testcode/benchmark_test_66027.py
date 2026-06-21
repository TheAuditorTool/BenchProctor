# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time


async def BenchmarkTest66027(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
