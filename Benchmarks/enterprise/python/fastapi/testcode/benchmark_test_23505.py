# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23505(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
