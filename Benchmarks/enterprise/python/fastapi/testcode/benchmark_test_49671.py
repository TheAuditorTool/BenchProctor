# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


request_state: dict[str, str] = {}

async def BenchmarkTest49671(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return {"updated": True}
