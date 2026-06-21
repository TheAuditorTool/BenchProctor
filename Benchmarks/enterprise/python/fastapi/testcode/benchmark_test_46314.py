# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest46314(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
