# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21034(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
