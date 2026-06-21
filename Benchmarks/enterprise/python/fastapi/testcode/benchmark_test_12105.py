# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest12105(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
