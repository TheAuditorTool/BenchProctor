# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest66822(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
