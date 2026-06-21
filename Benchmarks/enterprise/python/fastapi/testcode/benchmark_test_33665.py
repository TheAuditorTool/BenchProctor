# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest33665(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
