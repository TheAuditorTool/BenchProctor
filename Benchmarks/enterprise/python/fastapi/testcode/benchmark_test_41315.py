# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41315(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
