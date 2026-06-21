# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25996(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
