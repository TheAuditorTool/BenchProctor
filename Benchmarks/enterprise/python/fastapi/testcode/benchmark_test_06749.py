# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06749(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    os.system('echo ' + str(xml_value))
    return {"updated": True}
