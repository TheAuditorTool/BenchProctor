# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest19706(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
