# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00830(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
