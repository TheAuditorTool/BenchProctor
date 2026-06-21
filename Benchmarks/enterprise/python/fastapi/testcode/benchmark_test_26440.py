# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26440(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
