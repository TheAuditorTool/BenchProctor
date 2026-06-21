# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def relay_value(value):
    return value

async def BenchmarkTest45568(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
