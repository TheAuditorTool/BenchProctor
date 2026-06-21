# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest69391(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    exec(str(data))
    return {"updated": True}
