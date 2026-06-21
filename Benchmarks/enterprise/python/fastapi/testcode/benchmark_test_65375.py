# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


async def BenchmarkTest65375(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
