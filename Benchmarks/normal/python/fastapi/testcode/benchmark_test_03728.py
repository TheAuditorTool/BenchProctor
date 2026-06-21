# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest03728(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    globals()['counter'] = int(xml_value)
    return {"updated": True}
