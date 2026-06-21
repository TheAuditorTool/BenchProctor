# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest36539(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
