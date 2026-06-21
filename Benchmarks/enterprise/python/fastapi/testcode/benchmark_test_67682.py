# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest67682(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    int(str(data))
    return {"updated": True}
