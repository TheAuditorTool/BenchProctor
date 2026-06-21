# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest52171(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
