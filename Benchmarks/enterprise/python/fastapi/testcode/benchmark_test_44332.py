# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest44332(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
