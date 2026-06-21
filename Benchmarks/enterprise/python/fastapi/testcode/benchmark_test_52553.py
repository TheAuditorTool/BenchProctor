# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52553(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
