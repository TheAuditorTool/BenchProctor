# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest02439(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
