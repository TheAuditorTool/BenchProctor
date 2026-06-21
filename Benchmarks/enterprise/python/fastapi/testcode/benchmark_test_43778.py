# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest43778(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
