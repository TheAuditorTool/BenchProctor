# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest56592(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    globals()['counter'] = int(data)
    return {"updated": True}
