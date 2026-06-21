# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest21816(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
