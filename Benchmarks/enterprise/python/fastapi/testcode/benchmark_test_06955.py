# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest06955(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
