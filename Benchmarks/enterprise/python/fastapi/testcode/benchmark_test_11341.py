# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest11341(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
