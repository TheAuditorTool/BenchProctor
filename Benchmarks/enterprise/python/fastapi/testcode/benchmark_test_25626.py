# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest25626(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    os.seteuid(65534)
    return {"updated": True}
