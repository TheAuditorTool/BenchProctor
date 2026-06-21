# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest10830(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    request.session['user'] = str(data)
    return {"updated": True}
