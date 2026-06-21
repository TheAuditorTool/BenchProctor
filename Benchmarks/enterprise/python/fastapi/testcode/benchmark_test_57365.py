# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest57365(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = default_blank(xml_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
