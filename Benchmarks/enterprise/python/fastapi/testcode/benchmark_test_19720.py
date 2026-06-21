# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest19720(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    os.remove(str(data))
    return {"updated": True}
