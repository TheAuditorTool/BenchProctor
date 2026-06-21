# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12941(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(config_value), max_age=86400)
    return resp
