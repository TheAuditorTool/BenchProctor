# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15347(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
