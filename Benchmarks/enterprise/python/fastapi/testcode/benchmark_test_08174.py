# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08174(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
