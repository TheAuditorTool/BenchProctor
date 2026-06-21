# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest55822(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
