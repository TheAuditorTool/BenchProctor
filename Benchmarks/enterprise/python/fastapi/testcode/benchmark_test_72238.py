# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72238(request: Request):
    origin_value = request.headers.get('origin', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(origin_value))
    return {"updated": True}
