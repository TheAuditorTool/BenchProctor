# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44771(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
