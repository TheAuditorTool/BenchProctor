# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest46509(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
