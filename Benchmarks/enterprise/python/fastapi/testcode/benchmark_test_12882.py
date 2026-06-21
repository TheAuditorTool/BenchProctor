# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12882(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
