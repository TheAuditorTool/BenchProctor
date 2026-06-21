# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39719(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
