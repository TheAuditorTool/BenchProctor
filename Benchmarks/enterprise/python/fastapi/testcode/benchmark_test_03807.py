# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest03807(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    os.remove(str(data))
    return {"updated": True}
