# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import importlib


async def BenchmarkTest16955(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    importlib.import_module(str(data))
    return {"updated": True}
