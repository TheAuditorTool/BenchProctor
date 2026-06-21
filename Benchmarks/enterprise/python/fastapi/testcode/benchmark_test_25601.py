# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest25601(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
