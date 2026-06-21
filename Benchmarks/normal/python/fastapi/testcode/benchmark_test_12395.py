# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest12395(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    os.seteuid(65534)
    return {"updated": True}
