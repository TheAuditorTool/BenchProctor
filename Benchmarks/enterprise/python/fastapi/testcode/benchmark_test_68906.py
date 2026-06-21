# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest68906(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
