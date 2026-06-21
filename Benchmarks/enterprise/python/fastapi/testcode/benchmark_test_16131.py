# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest16131(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
