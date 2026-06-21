# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60478(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    int(str(data))
    return {"updated": True}
