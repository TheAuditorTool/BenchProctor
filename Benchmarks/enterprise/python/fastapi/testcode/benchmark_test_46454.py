# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest46454(request: Request):
    upload_name = (await request.form()).get('upload', '')
    link_path = os.path.join('/var/app/data', str(upload_name))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
