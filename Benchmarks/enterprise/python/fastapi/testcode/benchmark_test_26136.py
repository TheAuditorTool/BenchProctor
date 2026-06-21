# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest26136(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.seteuid(65534)
    return {"updated": True}
