# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest28515(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    int(str(data))
    return {"updated": True}
