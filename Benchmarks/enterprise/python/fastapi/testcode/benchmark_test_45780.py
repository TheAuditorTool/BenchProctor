# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest45780(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
