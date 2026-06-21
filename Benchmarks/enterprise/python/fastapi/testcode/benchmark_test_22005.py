# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest22005(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
