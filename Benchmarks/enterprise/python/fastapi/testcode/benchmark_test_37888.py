# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37888(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    int(str(data))
    return {"updated": True}
