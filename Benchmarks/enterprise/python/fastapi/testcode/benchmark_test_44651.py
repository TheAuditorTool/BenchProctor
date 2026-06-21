# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest44651(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
