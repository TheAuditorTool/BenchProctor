# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest03477(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
