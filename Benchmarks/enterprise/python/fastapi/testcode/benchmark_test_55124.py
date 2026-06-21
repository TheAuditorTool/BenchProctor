# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest55124(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
