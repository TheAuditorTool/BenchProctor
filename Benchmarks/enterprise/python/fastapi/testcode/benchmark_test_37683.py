# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37683(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
