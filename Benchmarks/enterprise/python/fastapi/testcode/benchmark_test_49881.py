# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49881(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return JSONResponse({'error': str(upload_name), 'stack': repr(locals())}, status_code=500)
