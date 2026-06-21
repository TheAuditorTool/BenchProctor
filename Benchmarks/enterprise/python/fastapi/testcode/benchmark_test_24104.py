# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import RedirectResponse
import urllib.parse


request_state: dict[str, str] = {}

async def BenchmarkTest24104(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
