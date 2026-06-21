# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37557(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
