# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from lxml import etree
from app_runtime import db


async def BenchmarkTest22737(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
