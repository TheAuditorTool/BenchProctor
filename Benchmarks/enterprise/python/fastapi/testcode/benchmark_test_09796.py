# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09796(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
