# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest72707(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    auth_check('user', data)
    return {"updated": True}
