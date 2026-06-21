# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06044(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
