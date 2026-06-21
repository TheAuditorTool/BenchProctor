# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os


async def BenchmarkTest23588(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
