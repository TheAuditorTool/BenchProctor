# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80092(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
