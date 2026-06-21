# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest54308(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    os.remove(str(data))
    return {"updated": True}
