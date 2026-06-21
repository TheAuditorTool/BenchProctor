# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09525(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    exec(str(data))
    return {"updated": True}
