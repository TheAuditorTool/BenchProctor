# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15442(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
