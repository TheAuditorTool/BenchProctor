# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
import os


async def BenchmarkTest64328(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
