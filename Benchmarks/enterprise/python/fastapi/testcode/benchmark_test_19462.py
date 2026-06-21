# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest19462(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    json.loads(data)
    return {"updated": True}
