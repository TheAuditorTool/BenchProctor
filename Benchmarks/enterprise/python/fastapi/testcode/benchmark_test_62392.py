# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62392(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
