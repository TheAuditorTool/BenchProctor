# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56610(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
