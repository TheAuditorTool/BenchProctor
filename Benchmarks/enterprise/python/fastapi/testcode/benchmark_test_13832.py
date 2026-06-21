# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13832(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
