# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest06608(request: Request, field: str = Form('')):
    field_value = field
    request.session['data'] = str(field_value)
    return {"updated": True}
