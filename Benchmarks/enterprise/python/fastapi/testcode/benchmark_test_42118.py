# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest42118(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    return HTMLResponse('<html><body><h1>' + str(xml_value) + '</h1></body></html>')
