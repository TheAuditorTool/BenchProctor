# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest33000(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = normalise_input(upload_name)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
