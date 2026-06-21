# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest56017(request: Request):
    origin_value = request.headers.get('origin', '')
    return HTMLResponse('<div>' + str(origin_value) + '</div>')
