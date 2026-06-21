# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest47726(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
