# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79557(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % str(xml_value)
    eval(str(data))
    return {"updated": True}
