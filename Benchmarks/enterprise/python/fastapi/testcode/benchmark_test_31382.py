# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31382(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
