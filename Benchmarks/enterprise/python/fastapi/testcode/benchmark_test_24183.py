# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24183(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    eval(str(env_value))
    return {"updated": True}
