# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import defusedxml.ElementTree


async def BenchmarkTest55280(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
