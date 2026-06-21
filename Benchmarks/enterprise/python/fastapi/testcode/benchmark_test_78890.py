# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest78890(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    json.loads(data)
    return {"updated": True}
