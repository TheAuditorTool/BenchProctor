# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest38361(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
