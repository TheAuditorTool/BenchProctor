# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest63287(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    request.session['data'] = str(data)
    return {"updated": True}
