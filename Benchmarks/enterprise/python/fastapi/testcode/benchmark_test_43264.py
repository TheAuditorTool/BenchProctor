# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest43264(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JSONResponse({'error': 'zero division'}, status_code=400)
    result = 100 / divisor
    return {"updated": True}
