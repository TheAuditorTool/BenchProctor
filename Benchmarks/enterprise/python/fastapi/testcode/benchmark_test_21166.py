# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest21166(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
