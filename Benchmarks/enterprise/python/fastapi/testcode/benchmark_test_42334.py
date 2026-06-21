# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest42334(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
