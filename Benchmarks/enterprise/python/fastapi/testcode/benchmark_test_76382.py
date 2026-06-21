# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest76382(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
