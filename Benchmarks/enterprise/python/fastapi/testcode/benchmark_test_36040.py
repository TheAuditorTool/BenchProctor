# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36040(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
