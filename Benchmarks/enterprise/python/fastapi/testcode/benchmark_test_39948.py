# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest39948(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    return HTMLResponse('<div>' + str(data) + '</div>')
