# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44010(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(multipart_value)})
