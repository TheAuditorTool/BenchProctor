# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest23967(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
