# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78987(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
