# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import socket


async def BenchmarkTest18309(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
