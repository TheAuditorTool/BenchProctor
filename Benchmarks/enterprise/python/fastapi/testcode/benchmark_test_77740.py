# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77740(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
