# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest04761(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    json.loads(data)
    return {"updated": True}
