# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest67056(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
