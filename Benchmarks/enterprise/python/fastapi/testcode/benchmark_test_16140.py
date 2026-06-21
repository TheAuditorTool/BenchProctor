# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest16140(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
