# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest27362(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
