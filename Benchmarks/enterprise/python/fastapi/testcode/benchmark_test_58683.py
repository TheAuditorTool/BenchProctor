# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58683(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    request.session['data'] = str(data)
    return {"updated": True}
