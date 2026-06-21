# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


async def BenchmarkTest07753(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    importlib.import_module(str(data))
    return {"updated": True}
