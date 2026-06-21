# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest79353(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
