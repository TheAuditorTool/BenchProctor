# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04079(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
