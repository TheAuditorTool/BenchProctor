# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest21686(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
