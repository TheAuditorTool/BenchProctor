# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest11671(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
