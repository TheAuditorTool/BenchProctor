# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


async def BenchmarkTest47298(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    importlib.import_module(str(env_value))
    return {"updated": True}
