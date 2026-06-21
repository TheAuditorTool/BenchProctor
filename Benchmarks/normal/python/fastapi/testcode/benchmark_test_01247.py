# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01247(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
