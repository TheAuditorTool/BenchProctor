# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest40822(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
