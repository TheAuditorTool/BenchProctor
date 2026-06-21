# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17741(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
