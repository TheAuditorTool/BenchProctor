# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from app_runtime import auth_check


async def BenchmarkTest01044(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
