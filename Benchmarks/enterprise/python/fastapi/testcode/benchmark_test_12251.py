# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest12251(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
