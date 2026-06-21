# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest09237(request: Request):
    path_value = request.path_params.get('id', '')
    data = ensure_str(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
