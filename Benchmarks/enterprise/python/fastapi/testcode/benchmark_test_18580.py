# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest18580(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    logging.info('User action: ' + str(data))
    return {"updated": True}
