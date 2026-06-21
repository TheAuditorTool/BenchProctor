# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23867(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
