# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20816(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
