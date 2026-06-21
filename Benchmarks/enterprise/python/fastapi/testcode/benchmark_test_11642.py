# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest11642(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
