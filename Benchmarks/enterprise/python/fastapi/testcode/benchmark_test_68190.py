# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest68190(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    processed = data[:64]
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
