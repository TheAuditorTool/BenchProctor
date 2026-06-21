# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51026(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
