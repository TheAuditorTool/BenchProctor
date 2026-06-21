# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest75834(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    return HTMLResponse(str(data))
