# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05845(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
