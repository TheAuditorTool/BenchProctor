# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote


async def BenchmarkTest21870(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
