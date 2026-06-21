# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00290(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    os.seteuid(65534)
    return {"updated": True}
