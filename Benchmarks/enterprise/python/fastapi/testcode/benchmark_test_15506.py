# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest15506(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
