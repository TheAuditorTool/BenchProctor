# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest48404(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
