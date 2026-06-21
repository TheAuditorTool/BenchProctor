# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest34243(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return HTMLResponse('<div>' + str(data) + '</div>')
