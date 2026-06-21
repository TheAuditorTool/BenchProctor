# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10386(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
