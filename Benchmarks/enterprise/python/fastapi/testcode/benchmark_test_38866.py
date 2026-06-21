# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38866(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    with open('/var/app/data/' + str(raw_body), 'r') as fh:
        content = fh.read()
    return content
