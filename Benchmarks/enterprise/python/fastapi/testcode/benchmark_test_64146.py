# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64146(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
