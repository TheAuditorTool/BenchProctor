# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest71274(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
