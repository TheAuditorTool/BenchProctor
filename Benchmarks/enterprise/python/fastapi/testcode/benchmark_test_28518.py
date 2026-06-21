# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


async def BenchmarkTest28518(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    globals()['counter'] = int(data)
    return {"updated": True}
