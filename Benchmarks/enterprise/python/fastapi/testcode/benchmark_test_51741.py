# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51741(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
