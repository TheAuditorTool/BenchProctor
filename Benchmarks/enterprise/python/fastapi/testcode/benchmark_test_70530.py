# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70530(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
