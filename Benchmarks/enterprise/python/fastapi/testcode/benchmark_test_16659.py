# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import importlib


async def BenchmarkTest16659(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
