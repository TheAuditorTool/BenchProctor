# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27740(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    exec(str(data))
    return {"updated": True}
