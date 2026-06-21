# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43395(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % (xml_value,)
    int(str(data))
    return {"updated": True}
