# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest50769(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    json.loads(data)
    return {"updated": True}
