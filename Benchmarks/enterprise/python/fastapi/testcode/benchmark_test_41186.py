# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest41186(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
