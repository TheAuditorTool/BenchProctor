# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest33917(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
