# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest29377(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
