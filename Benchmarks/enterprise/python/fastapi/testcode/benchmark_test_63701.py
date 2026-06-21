# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest63701(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    requests.get(str(cookie_value))
    return {"updated": True}
