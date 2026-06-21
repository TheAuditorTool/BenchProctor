# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote


async def BenchmarkTest03603(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
