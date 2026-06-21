# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77205(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    result = 100 / int(str(data))
    return {"updated": True}
