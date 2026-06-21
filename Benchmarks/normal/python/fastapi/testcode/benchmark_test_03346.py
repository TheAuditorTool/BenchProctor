# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import socket
from types import SimpleNamespace


async def BenchmarkTest03346(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return {"updated": True}
