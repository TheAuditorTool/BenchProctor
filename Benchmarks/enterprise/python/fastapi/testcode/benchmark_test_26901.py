# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def ensure_str(value):
    return str(value)

async def BenchmarkTest26901(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    globals()['counter'] = int(data)
    return {"updated": True}
