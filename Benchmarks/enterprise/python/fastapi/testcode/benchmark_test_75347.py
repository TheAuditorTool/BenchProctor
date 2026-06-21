# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest75347(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    eval(compile('s = socket.create_connection((str(data), 80))\ns.close()', '<sink>', 'exec'))
    return {"updated": True}
