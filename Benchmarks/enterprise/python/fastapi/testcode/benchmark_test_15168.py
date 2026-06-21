# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15168(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    eval(str(data))
    return {"updated": True}
