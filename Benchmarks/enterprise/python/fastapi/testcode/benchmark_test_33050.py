# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest33050(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = to_text(multipart_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
