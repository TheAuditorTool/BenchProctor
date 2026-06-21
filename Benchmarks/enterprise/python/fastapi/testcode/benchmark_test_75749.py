# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest75749(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request.session['user'] = str(env_value)
    return {"updated": True}
