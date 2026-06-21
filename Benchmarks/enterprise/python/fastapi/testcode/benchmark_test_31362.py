# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31362(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    int(str(data))
    return {"updated": True}
