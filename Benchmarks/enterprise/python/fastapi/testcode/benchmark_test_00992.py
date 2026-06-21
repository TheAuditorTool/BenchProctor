# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest00992(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
