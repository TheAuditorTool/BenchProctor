# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest09862(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    logging.info('User action: ' + str(data))
    return {"updated": True}
