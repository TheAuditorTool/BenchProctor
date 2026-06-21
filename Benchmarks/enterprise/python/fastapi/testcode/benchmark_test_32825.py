# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest32825(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = default_blank(xml_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
