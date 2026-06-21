# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest62136(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    json.loads(data)
    return {"updated": True}
