# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79264(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    int(str(data))
    return {"updated": True}
