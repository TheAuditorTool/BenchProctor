# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest41430(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.seteuid(65534)
    return {"updated": True}
