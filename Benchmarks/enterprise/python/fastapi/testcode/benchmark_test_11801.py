# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest11801(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
