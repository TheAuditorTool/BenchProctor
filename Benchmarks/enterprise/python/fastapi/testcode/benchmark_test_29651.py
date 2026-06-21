# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest29651(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    result = 100 / int(str(data))
    return {"updated": True}
