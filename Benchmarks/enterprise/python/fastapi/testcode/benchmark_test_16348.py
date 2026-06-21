# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest16348(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
