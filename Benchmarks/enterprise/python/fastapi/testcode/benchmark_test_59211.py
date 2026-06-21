# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59211(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
