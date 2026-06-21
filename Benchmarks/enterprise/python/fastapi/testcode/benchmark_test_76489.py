# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76489(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
