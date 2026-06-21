# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest00420(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    json.loads(data)
    return {"updated": True}
