# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


def normalise_input(value):
    return value.strip()

async def BenchmarkTest68652(request: Request):
    path_value = request.path_params.get('id', '')
    data = normalise_input(path_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
