# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest61206(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
