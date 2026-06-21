# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


async def BenchmarkTest09377(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return {"updated": True}
