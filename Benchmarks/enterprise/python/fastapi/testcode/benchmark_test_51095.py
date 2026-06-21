# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest51095(request: Request):
    path_value = request.path_params.get('id', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(path_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
