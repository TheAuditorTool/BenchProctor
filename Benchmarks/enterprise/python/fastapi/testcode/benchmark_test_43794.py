# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest43794(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
