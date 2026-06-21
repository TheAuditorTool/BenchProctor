# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest81265(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return {"updated": True}
