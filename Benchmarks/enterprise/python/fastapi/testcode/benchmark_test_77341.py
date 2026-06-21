# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77341(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
