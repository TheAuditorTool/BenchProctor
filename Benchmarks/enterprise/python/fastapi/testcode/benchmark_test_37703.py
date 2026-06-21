# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest37703(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
