# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest56353(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
