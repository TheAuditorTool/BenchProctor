# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest65481(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    int(str(env_value))
    return {"updated": True}
