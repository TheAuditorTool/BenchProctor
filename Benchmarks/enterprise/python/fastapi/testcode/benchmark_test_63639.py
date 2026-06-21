# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest63639(request: Request):
    query_array = request.query_params.get('items', '')
    reader = make_reader(query_array)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
