# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest10542(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
