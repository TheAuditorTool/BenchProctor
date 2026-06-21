# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import requests


async def BenchmarkTest10401(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
