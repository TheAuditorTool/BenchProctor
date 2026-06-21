# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest47787(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    processed = data[:64]
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
