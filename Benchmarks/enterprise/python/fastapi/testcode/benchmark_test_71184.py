# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest71184(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    os.system('echo ' + str(data))
    return {"updated": True}
