# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38571(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
