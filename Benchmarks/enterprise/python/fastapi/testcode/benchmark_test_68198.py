# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


async def BenchmarkTest68198(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(env_value) + '"]')
    return {"updated": True}
