# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04753(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    int(str(data))
    return {"updated": True}
