# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest15874(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return {"updated": True}
