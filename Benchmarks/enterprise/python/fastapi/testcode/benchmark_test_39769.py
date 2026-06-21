# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39769(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    os.seteuid(65534)
    return {"updated": True}
