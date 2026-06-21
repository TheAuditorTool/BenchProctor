# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
import os
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest73235(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
