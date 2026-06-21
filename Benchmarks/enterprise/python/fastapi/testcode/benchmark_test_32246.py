# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest32246(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
