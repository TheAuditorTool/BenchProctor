# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from app_runtime import db


async def BenchmarkTest22555(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
