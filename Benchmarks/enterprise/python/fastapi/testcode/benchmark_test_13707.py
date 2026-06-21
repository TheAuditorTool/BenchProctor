# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest13707(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
