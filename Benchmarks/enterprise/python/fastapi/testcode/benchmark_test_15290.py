# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


async def BenchmarkTest15290(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
