# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27033(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
