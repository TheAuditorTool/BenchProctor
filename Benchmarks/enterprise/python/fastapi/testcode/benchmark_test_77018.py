# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest77018(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        os.setuid(int(str(upload_name)) if str(upload_name).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
