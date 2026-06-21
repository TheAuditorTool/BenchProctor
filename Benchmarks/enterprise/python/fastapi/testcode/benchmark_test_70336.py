# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70336(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
