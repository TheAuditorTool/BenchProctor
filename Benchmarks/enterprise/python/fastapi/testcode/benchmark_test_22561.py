# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from starlette.responses import HTMLResponse


async def BenchmarkTest22561(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
