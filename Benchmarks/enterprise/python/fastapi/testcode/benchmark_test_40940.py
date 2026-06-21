# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest40940(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
