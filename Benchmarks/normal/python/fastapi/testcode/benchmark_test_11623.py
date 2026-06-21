# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest11623(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
