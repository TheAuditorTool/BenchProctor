# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest18290(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
