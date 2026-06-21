# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59645(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
