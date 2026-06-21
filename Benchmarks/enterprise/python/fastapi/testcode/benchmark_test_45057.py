# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest45057(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    globals()['counter'] = int(data)
    return {"updated": True}
