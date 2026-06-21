# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50585(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    request.session['user'] = str(data)
    return {"updated": True}
