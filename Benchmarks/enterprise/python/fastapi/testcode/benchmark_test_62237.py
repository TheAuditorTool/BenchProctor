# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest62237(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
