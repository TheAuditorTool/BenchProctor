# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest69936(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
