# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import json


async def BenchmarkTest57680(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
