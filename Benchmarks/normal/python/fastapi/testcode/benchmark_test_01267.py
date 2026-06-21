# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest01267(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    json.loads(data)
    return {"updated": True}
