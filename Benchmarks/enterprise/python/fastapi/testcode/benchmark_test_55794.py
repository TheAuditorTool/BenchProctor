# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def normalise_input(value):
    return value.strip()

async def BenchmarkTest55794(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
