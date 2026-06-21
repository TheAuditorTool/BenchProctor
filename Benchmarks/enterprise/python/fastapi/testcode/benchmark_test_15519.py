# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest15519(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
