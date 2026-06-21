# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import importlib


async def BenchmarkTest17534(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
