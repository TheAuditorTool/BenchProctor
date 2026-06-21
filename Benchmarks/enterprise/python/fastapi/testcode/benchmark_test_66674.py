# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66674(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
