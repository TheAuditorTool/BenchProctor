# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest25614(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
