# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest65819(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    defusedxml.ElementTree.fromstring(str(cookie_value))
    return {"updated": True}
