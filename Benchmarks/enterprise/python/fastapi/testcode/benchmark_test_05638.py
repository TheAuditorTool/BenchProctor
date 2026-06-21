# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05638(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    with open('output.csv', 'a') as fh:
        fh.write(str(xml_value) + ',data\n')
    return {"updated": True}
