# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest02409(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
