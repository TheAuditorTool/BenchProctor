# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest26593(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
