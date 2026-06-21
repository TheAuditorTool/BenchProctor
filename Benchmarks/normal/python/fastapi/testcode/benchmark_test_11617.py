# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest11617(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    yaml.safe_load(cookie_value)
    return {"updated": True}
