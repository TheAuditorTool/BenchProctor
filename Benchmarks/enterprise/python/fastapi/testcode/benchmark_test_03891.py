# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest03891(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    logging.info('User action: ' + str(data))
    return {"updated": True}
