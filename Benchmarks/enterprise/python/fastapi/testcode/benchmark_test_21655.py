# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21655(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
