# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest31687(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
