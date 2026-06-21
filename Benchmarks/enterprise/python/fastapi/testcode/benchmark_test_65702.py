# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65702(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    request.session['user'] = str(data)
    return {"updated": True}
