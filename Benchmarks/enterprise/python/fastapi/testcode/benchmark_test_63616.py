# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63616(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
