# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest53323(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
