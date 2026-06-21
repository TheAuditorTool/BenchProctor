# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest28763(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
