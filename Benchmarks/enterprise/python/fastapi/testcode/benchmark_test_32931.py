# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest32931(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
