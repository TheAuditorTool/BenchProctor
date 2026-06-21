# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78294(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
