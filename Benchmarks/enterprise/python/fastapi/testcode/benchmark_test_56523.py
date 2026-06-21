# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest56523(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
