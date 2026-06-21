# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest07104(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
