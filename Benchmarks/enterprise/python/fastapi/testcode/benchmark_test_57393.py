# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest57393(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
