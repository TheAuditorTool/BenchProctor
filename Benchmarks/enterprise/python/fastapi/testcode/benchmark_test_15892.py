# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15892(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
