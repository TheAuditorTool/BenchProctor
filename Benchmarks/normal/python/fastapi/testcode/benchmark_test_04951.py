# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest04951(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    os.setuid(int(str(env_value)) if str(env_value).isdigit() else 0)
    return {"updated": True}
