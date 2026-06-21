# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest69230(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
