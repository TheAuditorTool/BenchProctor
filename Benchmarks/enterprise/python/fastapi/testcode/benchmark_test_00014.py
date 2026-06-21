# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00014(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
