# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest56162(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
