# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest17436(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
