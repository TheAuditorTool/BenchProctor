# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest55287(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    os.system('echo ' + str(data))
    return {"updated": True}
