# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17324(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
