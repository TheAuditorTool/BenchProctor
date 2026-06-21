# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest06963(request: Request):
    upload_name = (await request.form()).get('upload', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(upload_name), secure=True, httponly=True, samesite='Strict')
    return resp
