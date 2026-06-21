# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38402(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % (xml_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
