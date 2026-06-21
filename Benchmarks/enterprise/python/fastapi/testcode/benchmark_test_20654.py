# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest20654(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
