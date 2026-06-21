# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest12980(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = handle(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
