# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def normalise_input(value):
    return value.strip()

async def BenchmarkTest07776(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    processed = data[:64]
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(processed)})
