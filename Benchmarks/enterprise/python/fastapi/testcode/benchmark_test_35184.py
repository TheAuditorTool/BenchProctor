# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35184(request: Request):
    referer_value = request.headers.get('referer', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(referer_value))
    return {"updated": True}
