# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest52849(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
