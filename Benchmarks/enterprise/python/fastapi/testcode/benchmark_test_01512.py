# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01512(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    result = 100 / int(str(data))
    return {"updated": True}
