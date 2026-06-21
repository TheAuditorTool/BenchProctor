# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38723(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
