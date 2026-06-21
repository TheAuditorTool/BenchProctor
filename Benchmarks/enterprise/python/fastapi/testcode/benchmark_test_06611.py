# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
from app_runtime import auth_check


async def BenchmarkTest06611(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    auth_check('user', data)
    return {"updated": True}
