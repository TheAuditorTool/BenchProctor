# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest00768(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
