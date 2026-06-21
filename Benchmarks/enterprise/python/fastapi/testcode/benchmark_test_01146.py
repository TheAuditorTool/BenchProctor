# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01146(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
