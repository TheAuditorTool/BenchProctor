# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest71112(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
