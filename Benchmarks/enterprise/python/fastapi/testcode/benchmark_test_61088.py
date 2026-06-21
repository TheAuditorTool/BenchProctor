# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest61088(request: Request):
    stdin_value = input('input: ')
    data = FormData(payload=stdin_value).payload
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
