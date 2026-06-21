# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49980(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
