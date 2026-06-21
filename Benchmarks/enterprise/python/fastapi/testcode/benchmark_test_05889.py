# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05889(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
