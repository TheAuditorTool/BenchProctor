# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest52500(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
