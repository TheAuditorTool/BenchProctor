# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60978(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
