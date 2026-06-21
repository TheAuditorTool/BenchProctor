# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


async def BenchmarkTest25311(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    importlib.import_module(str(data))
    return {"updated": True}
