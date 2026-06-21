# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest26415(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
