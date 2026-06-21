# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def normalise_input(value):
    return value.strip()

async def BenchmarkTest12396(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    processed = str(data).replace("<script", "")
    return HTMLResponse('<div>' + str(processed) + '</div>')
