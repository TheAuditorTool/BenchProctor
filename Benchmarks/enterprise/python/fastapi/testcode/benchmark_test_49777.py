# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest49777(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
