# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest52611(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
