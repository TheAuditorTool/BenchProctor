# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03914(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
