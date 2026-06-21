# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest10189(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    globals()['counter'] = int(data)
    return {"updated": True}
