# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest08685(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
