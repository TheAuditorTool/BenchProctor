# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest71659(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
