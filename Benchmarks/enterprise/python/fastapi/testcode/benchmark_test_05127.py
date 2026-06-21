# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest05127(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
