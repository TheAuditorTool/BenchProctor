# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest77697(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
