# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45972(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    os.remove(str(data))
    return {"updated": True}
