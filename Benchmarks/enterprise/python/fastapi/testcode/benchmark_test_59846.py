# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59846(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
