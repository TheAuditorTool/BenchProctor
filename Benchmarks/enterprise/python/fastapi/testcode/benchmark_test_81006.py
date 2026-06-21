# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest81006(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
