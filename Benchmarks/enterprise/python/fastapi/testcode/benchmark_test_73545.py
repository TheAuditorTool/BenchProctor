# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73545(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
