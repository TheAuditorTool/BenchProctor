# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72864(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
