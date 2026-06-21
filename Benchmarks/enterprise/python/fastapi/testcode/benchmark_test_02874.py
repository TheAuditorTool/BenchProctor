# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def normalise_input(value):
    return value.strip()

async def BenchmarkTest02874(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
