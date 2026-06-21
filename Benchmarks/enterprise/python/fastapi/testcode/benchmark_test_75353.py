# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest75353(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return RedirectResponse(url=str(data))
