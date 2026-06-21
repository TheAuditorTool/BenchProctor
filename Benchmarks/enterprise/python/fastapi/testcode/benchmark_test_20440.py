# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest20440(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
