# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59578(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
