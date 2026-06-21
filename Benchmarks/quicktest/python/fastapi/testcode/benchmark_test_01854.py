# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest01854(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
