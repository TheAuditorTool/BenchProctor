# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote


async def BenchmarkTest40767(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    logging.info('User action: ' + str(data))
    return {"updated": True}
