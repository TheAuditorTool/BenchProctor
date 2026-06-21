# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import tempfile


async def BenchmarkTest65256(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
