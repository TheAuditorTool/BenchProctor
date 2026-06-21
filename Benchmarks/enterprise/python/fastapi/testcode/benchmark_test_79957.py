# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79957(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
