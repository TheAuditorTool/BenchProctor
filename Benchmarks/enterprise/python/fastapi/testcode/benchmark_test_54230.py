# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest54230(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
