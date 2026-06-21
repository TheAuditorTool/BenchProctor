# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form
import time


async def BenchmarkTest55074(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
