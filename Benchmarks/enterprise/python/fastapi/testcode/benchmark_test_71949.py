# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest71949(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
