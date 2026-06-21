# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10035(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
