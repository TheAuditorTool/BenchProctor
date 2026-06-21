# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest78625(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
