# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest09974(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
