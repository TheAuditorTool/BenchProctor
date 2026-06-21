# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest45708(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
