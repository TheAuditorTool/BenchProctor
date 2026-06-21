# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28060(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    request.session['data'] = str(data)
    return {"updated": True}
