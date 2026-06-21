# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01466(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
