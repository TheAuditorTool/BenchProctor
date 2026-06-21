# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70280(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
