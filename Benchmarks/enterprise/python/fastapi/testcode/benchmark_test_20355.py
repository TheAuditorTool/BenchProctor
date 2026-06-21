# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest20355(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    os.system('echo ' + str(multipart_value))
    return {"updated": True}
