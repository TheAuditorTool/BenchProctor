# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42680(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    eval(str(data))
    return {"updated": True}
