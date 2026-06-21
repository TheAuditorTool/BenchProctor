# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79959(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
