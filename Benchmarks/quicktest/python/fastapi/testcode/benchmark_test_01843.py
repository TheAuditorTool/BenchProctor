# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import defusedxml.ElementTree


async def BenchmarkTest01843(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
