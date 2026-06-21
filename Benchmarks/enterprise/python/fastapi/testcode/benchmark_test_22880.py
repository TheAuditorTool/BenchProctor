# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest22880(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    os.remove(str(data))
    return {"updated": True}
