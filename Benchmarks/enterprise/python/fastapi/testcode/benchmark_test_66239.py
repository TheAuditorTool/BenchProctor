# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66239(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
