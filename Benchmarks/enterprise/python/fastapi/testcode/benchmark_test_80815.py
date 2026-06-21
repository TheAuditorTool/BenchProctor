# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80815(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
