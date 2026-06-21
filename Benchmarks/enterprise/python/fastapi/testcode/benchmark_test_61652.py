# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import os


async def BenchmarkTest61652(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return {"updated": True}
