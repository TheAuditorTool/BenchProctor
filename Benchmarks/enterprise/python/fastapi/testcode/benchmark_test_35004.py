# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest35004(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    request.session['user'] = str(data)
    return {"updated": True}
