# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest00275(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
