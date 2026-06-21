# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time


request_state: dict[str, str] = {}

async def BenchmarkTest07898(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return {"updated": True}
