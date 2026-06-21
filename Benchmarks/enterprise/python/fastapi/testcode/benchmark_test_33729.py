# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest33729(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    os.remove(str(data))
    return {"updated": True}
