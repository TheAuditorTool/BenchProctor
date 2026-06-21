# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest27565(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
