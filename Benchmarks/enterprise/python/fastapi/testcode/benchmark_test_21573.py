# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest21573(request: Request):
    upload_name = (await request.form()).get('upload', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(upload_name))
    return RedirectResponse(url=target)
