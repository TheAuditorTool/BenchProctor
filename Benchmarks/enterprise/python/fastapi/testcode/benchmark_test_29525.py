# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest29525(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    request.session['data'] = str(data)
    return {"updated": True}
