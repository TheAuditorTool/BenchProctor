# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest79000(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
