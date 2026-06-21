# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest41580(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    os.remove(str(data))
    return {"updated": True}
