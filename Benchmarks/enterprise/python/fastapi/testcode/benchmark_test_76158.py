# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76158(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
