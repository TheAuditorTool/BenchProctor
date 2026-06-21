# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53375(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    result = 100 / int(str(data))
    return {"updated": True}
