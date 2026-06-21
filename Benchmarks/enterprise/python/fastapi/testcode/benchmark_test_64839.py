# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest64839(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    json.loads(data)
    return {"updated": True}
