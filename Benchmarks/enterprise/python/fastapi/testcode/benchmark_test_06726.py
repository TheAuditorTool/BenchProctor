# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest06726(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
