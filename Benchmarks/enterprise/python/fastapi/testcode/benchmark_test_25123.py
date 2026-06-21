# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest25123(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    os.remove(str(data))
    return {"updated": True}
