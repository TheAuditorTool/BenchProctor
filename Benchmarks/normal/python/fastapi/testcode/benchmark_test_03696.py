# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest03696(request: Request):
    path_value = request.path_params.get('id', '')
    data = normalise_input(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
