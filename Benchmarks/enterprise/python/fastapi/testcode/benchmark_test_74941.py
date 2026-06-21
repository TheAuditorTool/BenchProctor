# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74941(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
