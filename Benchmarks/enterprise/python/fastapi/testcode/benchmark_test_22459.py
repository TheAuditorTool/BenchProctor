# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22459(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
