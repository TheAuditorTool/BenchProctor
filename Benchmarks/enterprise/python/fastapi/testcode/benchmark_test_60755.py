# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest60755(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
