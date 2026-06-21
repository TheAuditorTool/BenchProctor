# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44411(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    return JSONResponse({'error': str(multipart_value), 'stack': repr(locals())}, status_code=500)
