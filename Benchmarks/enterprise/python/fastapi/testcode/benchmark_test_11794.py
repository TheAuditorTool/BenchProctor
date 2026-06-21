# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


async def BenchmarkTest11794(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    importlib.import_module(str(data))
    return {"updated": True}
