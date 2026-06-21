# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


async def BenchmarkTest44827(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
