# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest33222(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
