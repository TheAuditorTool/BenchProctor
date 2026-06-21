# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest15627(request: Request):
    path_value = request.path_params.get('id', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(path_value))
    return RedirectResponse(url=target)
