# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31028(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
