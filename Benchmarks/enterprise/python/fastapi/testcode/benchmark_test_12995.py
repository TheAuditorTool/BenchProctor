# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest12995(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
