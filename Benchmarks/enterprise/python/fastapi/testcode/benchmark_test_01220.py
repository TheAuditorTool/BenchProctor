# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest01220(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    yaml.load(cookie_value, Loader=yaml.UnsafeLoader)
    return {"updated": True}
