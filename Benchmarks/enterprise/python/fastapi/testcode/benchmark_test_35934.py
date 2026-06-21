# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest35934(request: Request):
    path_value = request.path_params.get('id', '')
    logging.info('User action: ' + str(path_value))
    return {"updated": True}
