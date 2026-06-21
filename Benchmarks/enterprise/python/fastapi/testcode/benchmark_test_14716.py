# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import importlib
from types import SimpleNamespace


async def BenchmarkTest14716(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
