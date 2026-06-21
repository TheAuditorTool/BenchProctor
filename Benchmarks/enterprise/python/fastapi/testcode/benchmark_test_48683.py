# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48683(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
