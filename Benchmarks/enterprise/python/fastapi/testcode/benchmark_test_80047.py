# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest80047(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    auth_check('user', env_value)
    return {"updated": True}
