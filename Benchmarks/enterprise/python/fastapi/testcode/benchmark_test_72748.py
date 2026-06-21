# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def relay_value(value):
    return value

async def BenchmarkTest72748(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    logging.info('User action: ' + str(data))
    return {"updated": True}
