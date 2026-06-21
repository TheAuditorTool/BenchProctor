# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest58492(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
