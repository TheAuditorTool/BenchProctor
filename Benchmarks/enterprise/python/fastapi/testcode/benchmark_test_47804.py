# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47804(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
