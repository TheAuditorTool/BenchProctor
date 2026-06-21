# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest54177(request: Request):
    user_id = request.query_params.get('id', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(user_id),))
    logging.info('request processed')
    return {"updated": True}
