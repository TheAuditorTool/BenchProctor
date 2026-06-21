# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest76242(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
