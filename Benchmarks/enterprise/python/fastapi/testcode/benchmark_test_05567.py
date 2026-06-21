# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest05567(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
