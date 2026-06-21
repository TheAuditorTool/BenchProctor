# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from lxml import etree
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11000(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
