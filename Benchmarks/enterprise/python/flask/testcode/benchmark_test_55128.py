# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest55128():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
