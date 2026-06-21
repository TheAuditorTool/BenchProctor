# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02061(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
