# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest71337(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
