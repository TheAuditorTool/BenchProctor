# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest29890(request: Request):
    user_id = request.query_params.get('id', '')
    logging.info('User action: ' + str(user_id))
    return {"updated": True}
