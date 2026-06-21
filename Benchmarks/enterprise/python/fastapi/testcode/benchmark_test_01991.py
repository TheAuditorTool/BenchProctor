# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01991(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
