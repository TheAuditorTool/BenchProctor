# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest77326(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
