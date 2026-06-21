# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest46860(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
