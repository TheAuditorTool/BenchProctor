# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest45973(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(upload_name) + ' -->')
