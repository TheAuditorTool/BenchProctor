# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest65704(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
