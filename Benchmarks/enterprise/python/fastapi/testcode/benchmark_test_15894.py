# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15894(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(upload_name)})
