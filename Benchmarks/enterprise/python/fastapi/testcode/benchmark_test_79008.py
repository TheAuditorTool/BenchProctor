# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79008(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % (xml_value,)
    request.session['data'] = str(data)
    return {"updated": True}
