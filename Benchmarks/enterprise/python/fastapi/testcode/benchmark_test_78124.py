# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78124(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
