# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest46898(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    return HTMLResponse(str(data))
