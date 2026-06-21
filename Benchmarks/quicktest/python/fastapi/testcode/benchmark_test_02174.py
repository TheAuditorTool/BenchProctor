# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02174(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    os.system('echo ' + str(data))
    return {"updated": True}
