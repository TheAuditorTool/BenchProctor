# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from fastapi import Form


def normalise_input(value):
    return value.strip()

async def BenchmarkTest05400(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
