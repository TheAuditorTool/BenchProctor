# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest02312(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    os.remove(str(data))
    return {"updated": True}
