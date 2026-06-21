# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest65277(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
