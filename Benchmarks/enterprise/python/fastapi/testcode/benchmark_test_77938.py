# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest77938(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    os.system('echo ' + str(data))
    return {"updated": True}
