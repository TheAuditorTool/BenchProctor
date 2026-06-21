# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04641(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    with open('/var/app/data/' + str(xml_value), 'r') as fh:
        content = fh.read()
    return content
