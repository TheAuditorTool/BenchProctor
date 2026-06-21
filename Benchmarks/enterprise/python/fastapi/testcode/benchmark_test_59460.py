# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest59460(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    os.seteuid(65534)
    return {"updated": True}
