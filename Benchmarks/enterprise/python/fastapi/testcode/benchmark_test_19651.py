# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest19651(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
