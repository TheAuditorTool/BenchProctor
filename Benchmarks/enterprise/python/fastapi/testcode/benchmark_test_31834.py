# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


async def BenchmarkTest31834(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
