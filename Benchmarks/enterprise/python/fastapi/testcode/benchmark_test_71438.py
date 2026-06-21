# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import defusedxml.ElementTree


async def BenchmarkTest71438(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
