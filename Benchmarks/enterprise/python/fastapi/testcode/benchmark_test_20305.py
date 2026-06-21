# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20305(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request.session['data'] = str(xml_value)
    return {"updated": True}
