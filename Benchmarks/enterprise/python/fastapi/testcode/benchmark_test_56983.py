# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest56983(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
