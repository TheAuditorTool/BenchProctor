# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53164(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
