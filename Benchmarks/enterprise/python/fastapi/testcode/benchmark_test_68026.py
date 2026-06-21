# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest68026(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    int(str(data))
    return {"updated": True}
