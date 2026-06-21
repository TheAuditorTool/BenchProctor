# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


async def BenchmarkTest58599(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    importlib.import_module(str(data))
    return {"updated": True}
