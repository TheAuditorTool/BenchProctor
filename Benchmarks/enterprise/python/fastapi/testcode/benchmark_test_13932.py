# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest13932(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
