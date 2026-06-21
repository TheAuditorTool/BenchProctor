# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02603(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
