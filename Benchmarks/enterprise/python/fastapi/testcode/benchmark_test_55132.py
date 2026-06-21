# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest55132(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
