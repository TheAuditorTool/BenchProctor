# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest46715(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    json.loads(data)
    return {"updated": True}
