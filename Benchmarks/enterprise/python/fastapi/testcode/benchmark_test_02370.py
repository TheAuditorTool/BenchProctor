# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02370(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    request.session['user'] = str(data)
    return {"updated": True}
