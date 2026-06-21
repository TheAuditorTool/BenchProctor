# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest30797(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
