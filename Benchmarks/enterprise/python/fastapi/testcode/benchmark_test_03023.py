# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from urllib.parse import unquote


async def BenchmarkTest03023(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
