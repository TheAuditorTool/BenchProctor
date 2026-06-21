# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78727(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
