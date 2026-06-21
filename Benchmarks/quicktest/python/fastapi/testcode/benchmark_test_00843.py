# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest00843(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
