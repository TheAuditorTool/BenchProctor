# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from lxml import etree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest41634(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    await _evasion_task()
    return {"updated": True}
