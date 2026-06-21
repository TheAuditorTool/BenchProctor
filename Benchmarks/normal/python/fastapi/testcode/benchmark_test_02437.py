# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02437(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
