# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest08877(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    return HTMLResponse(str(data))
