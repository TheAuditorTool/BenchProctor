# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08853(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
