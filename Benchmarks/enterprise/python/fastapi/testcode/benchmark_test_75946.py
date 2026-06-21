# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest75946(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
