# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import json
from app_runtime import db


async def BenchmarkTest65495(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
