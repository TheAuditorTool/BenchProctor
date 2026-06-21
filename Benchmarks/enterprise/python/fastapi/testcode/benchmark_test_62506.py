# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62506(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
