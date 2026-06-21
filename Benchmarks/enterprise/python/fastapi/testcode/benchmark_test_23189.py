# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest23189(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
