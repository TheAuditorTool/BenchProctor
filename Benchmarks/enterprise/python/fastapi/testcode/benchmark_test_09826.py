# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest09826(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
