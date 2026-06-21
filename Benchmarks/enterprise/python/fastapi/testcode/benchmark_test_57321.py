# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest57321(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JSONResponse({'action': action}, status_code=200)
