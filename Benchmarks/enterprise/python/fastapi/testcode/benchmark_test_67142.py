# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest67142(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
