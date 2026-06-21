# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest80173(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    os.remove(str(data))
    return {"updated": True}
