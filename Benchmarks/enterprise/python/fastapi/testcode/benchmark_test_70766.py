# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest70766(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
