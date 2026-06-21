# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest54320(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
