# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68287(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
