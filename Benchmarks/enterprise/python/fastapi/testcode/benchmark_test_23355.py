# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest23355(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    eval(str(data))
    return {"updated": True}
