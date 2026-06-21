# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest74021(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    logging.info('User action: ' + str(data))
    return {"updated": True}
