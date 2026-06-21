# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest23852(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = multipart_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
