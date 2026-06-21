# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72875(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    request.session['data'] = str(data)
    return {"updated": True}
