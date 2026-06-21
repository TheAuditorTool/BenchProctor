# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import defusedxml.ElementTree


async def BenchmarkTest56920(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
