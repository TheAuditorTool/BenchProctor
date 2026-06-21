# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest40729(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    eval(str(data))
    return {"updated": True}
