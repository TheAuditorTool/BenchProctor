# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest77146(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
