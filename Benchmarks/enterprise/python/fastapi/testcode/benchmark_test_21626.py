# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest21626(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
