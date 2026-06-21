# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest00549(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    request.session['user'] = str(data)
    return {"updated": True}
