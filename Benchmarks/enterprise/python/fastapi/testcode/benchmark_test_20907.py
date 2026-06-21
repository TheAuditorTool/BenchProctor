# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest20907(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<div>' + str(data) + '</div>')
