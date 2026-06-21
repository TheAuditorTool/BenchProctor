# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest42426(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = normalise_input(config_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
