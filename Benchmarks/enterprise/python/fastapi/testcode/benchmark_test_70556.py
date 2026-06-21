# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest70556(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    defusedxml.ElementTree.fromstring(str(raw_body))
    return {"updated": True}
