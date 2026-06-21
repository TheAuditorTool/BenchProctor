# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


async def BenchmarkTest69141(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
