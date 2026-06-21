# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import RedirectResponse
import urllib.parse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest30962(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
