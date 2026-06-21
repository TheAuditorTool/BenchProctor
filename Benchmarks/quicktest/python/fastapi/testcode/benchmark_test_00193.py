# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest00193(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    return HTMLResponse('<div>' + str(data) + '</div>')
