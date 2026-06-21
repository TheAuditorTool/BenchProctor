# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest38253(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return HTMLResponse('<img src="' + str(data) + '">')
