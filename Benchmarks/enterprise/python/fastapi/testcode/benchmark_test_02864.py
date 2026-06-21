# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest02864(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    request.session['data'] = str(data)
    return {"updated": True}
