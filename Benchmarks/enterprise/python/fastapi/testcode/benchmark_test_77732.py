# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77732(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
