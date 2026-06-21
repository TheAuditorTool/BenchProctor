# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest21804(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
